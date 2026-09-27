# fetch the research paper from pubmed that reference speciofic
# clinical trail ID. This is our 2nd data source.
# what it does:
# take the NCT id (e.g NCT093092)
# SEARCHES PUBMED FOR PAPERS THAT reference that trail.
# fetches the full abstract & metadata for each paper.
# return raw paper records - no cleaning happens here

# clinicaltrails.gov tells us what study was promised to measure
# Pubmed tells us what researchers actually published.
# Gap between those two things is where signals live.