# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "generic_theme"
app_title = "Generic ERPNext Website Theme"
app_publisher = "Said Salameh"
app_description = "Generic ERPNext Website Theme"
app_icon = "octicon octicon-globe"
app_color = "#1affa3"
app_email = "ss@saidsalameh.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/generic_theme/css/generic_theme.css"
# app_include_js = "/assets/generic_theme/js/generic_theme.js"

# include js, css files in header of web template
web_include_css = "/assets/css/mnt.min.css"
web_include_js = "/assets/js/mnt.min.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "generic_theme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "generic_theme.install.before_install"
# after_install = "generic_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "generic_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"generic_theme.tasks.all"
# 	],
# 	"daily": [
# 		"generic_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"generic_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"generic_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"generic_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "generic_theme.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "generic_theme.event.get_events"
# }

