import os
BACKEND = 'hcf_backend.HCFBackend'
HCF_PROJECT_ID = int(os.getenv('SCRAPY_PROJECT_ID'))
HCF_FRONTIER = 'surfacewalker'
#HCF_AUTH = 'override-in-local-settings'

JOBID = os.getenv('SCRAPY_JOB')
if JOBID:
    HCF_CONSUMER_SLOT = int(JOBID.split('/')[-1]) % 8
