
from invenio_records_resources.records.api import Record
from invenio_vocabularies.contrib.affiliations.affiliations import (
    record_type as record_type,
)

Affiliation: type[Record]
