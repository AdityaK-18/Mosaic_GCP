# entry point of all the data
# fetch all the clinical study records from clinicaltrails.gov
# connects to public api(say private for interview)
# searches all studies by condition, intervention or sponsor
# fetches full study details for each result
# handles pagination - returns 100 results per page
# handles rate limiting & retries automatically