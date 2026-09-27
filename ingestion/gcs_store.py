# save and load the documents to and from google cloud storage
# this is permanent storage layer for all the raw and parsed docs
# save raw api response to gcs bucket as JSON
# save parsed study and paper records to GCS as JSON
# loads documents back from GCS when agent needs them
# list available documents by prefix - useful for batch processing

# why we save the raw data 1st?

# if my parser has a bug, raw original are safe is GCS
# folder structure can you expect in the GCS
# raw/studies/NCT080909.json -> what api returned
# raw/paper/9873847.json -> exactly what pubmed returned
# processed/studies/NCT080909.json -> parsed paper as JSON
