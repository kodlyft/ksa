// Copyright (c) 2026, Kodlyft and contributors
// For license information, please see license.txt

frappe.ui.form.on("KSA VAT Setting", {
	setup: function (frm) {
		const tables = ["ksa_vat_purchase_accounts", "ksa_vat_sales_accounts"];

		const queries = {
			account: {
				account_type: "Tax",
				is_group: 0,
			},
			item_tax_template: {
				disabled: 0,
			},
		};

		tables.forEach((table) => {
			Object.keys(queries).forEach((field) => {
				frm.set_query(field, table, () => ({
					filters: queries[field],
				}));
			});
		});
	},

	onload: function () {
		frappe.breadcrumbs.add("Accounts", "KSA VAT Setting");
	},
});
