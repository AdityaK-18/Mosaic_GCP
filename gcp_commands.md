project name : mosaic-clinical-trails
gcloud auth login
Create GCS Bucket
create cloud SQL : act as relational db + vector db
create an instance 

#step1:
gcloud sql instances create clinical-trial-db \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --region=us-central1 \
  --project=clinical-trials-507909

gcloud sql instances list --project=clinical-trials-507909

# step2: create db inside instance
gcloud sql databases create clinical_trial_db \
  --instance=clinical-trial-db \
  --project=clinical-trials-507909

# step3: creating cloud sql user
gcloud sql users create mosaic_user \
  --instance=clinical-trial-db \
  --password=mosaic_pass_2026 \
  --project=clinical-trials-507909

# step4: whitelist of current ip address in personal system
 curl -4 ipconfig.me 
  49.37.161.38 (whitelist)

# the Cloud SQL instance's firewall-like allowlist:
gcloud sql instances patch clinical-trial-db \
  --authorized-networks=49.37.161.38/32 \
  --project=clinical-trials-507909

# install psql & connect to create the schema

MAC : brew install libpq

# Want me to add that to your .zshrc?
source ~/.zshrc

# connect to terminal to our db
! psql -h 35.193.7.108 -U mosaic_user -d clinical_trial_db