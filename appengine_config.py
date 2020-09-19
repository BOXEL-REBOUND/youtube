"""App Engine-specific configuration to bring in third-party
   libraries."""

# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')
