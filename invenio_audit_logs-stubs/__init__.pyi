from invenio_audit_logs.ext import InvenioAuditLogs as InvenioAuditLogs

# Export the same public API as the runtime package
__all__ = ("InvenioAuditLogs", "__version__")

__version__: str
