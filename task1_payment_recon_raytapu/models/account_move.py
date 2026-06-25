import re
from odoo import models

SO_REFERENCE_PATTERN = re.compile(r'SO\d+',re.IGNORECASE)

class AccountMoveLine(models.Model):
	_inherit = 'account.move.line'

def _extract_so_reference(self, label_text):
	if not label_text:
		return None
	match = SO_REFERENCE_PATTERN.search(label_text)
	if match:
		return match.group(0)
	return None
