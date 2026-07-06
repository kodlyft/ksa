# Copyright (c) 2026, Kodlyft and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class KSAVATSetting(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from ksa.ksa.doctype.ksa_vat_purchase_account.ksa_vat_purchase_account import KSAVATPurchaseAccount
		from ksa.ksa.doctype.ksa_vat_sales_account.ksa_vat_sales_account import KSAVATSalesAccount

		company: DF.Link
		ksa_vat_purchase_accounts: DF.Table[KSAVATPurchaseAccount]
		ksa_vat_sales_accounts: DF.Table[KSAVATSalesAccount]
	# end: auto-generated types

	pass
