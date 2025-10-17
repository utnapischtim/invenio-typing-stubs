
from invenio_records_resources.resources import RecordResource, RecordResourceConfig
from invenio_vocabularies.contrib.awards.awards import record_type as record_type

AwardsResourceConfig: type[RecordResourceConfig]
AwardsResource: type[RecordResource]
