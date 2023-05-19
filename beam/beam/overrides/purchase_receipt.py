import frappe
from erpnext.stock.doctype.purchase_receipt.purchase_receipt import PurchaseReceipt
from beam.beam.overrides.handling_unit_mixin import (
	HandlingUnitMixin,
	patched_make_sl_entries,
	patched_get_sl_entries,
)


class CustomPurchaseReceipt(PurchaseReceipt, HandlingUnitMixin):
	def on_submit(self):
		super().on_submit()

	def on_cancel(self):
		super().on_cancel()

	def before_submit(self):
		super().before_submit()

	def make_sl_entries(self, sl_entries, allow_negative_stock=False, via_landed_cost_voucher=False):
		patched_make_sl_entries(sl_entries, allow_negative_stock, via_landed_cost_voucher)

	def get_sl_entries(self, d, args):
		return patched_get_sl_entries(self, d, args)
