# run the entire ingestion pipeline
# run this file to fetch studies, fetch papers, parse everything
# and save it to the google cloud storage

# fetches studies from clinicaltrails.gov
# save the raw data to GCS bucket
# parse the raw studies into clean structural records
# save parsed records to GCS
# FOR EACH RESEARCH STUDY, fetch related research papers.
# save raw & parsed papers to GCS