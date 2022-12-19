# problem statement:
# Given a variable input- could be either a dict or a list of dict
# we need to print all keys as list and all values as another list.
# sample data can be downloaded from here ----- https://opensource.adobe.com/Spry/samples/data_region/JSONDataSetSample.html

# l = [{
#         'plan_code': 'b',
#         'quantity': '1',
#         'account': {
#             'account_code': 'b',
#             'username': 'jdoe',
#             'email': 'jdoe@domain.com',
#             'first_name': 'b',
#             'last_name': 'b',
#             'company_name': 'Company, LLC.',
#             'billing_info': {
#                 'first_name': 'b',
#                 'last_name': 'b',
#                 'address1': '123 Test St',
#                 'city': 'San Francisco',
#                 'state': 'CA',
#                 'country': 'US',
#                 'zip': '94105',
#                 'credit_card': {
#                     'number': '1',
#                     'year': '2018',
#                     'month': '12',
#                     'verification_value': '123',
#                 },
#             },
#         },
#     },
#   {
#     "items":
#       {
#         "item":
#           [
#             {
#               "id": "0001",
#               "type": "donut",
#               "name": "Cake",
#               "ppu": 0.55,
#               "batters":
#                 {
#                   "batter":
#                     [
#                       {"id": "1001", "type": "Regular"},
#                       {"id": "1002", "type": "Chocolate"},
#                       {"id": "1003", "type": "Blueberry"},
#                       {"id": "1004", "type": "Devil's Food"}
#                     ]
#                 },
#               "topping":
#                 [
#                   {"id": "5001", "type": "None"},
#                   {"id": "5002", "type": "Glazed"},
#                   {"id": "5005", "type": "Sugar"},
#                   {"id": "5007", "type": "Powdered Sugar"},
#                   {"id": "5006", "type": "Chocolate with Sprinkles"},
#                   {"id": "5003", "type": "Chocolate"},
#                   {"id": "5004", "type": "Maple"}
#                 ]
#             }
#           ]
#       }
#   },
# {
#     "glossary": {
#         "title": "example glossary",
# 		"GlossDiv": {
#             "title": "S",
# 			"GlossList": {
#                 "GlossEntry": {
#                     "ID": "SGML",
# 					"SortAs": "SGML",
# 					"GlossTerm": "Standard Generalized Markup Language",
# 					"Acronym": "SGML",
# 					"Abbrev": "ISO 8879:1986",
# 					"GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
# 						"GlossSeeAlso": ["GML", "XML"]
#                     },
# 					"GlossSee": "markup"
#                 }
#             }
#         }
#     }
# },
#   {"web-app": {
#     "servlet": [
#       {
#         "servlet-name": "cofaxCDS",
#         "servlet-class": "org.cofax.cds.CDSServlet",
#         "init-param": {
#           "configGlossary:installationAt": "Philadelphia, PA",
#           "configGlossary:adminEmail": "ksm@pobox.com",
#           "configGlossary:poweredBy": "Cofax",
#           "configGlossary:poweredByIcon": "/images/cofax.gif",
#           "configGlossary:staticPath": "/content/static",
#           "templateProcessorClass": "org.cofax.WysiwygTemplate",
#           "templateLoaderClass": "org.cofax.FilesTemplateLoader",
#           "templatePath": "templates",
#           "templateOverridePath": "",
#           "defaultListTemplate": "listTemplate.htm",
#           "defaultFileTemplate": "articleTemplate.htm",
#           "useJSP": False,
#           "jspListTemplate": "listTemplate.jsp",
#           "jspFileTemplate": "articleTemplate.jsp",
#           "cachePackageTagsTrack": 200,
#           "cachePackageTagsStore": 200,
#           "cachePackageTagsRefresh": 60,
#           "cacheTemplatesTrack": 100,
#           "cacheTemplatesStore": 50,
#           "cacheTemplatesRefresh": 15,
#           "cachePagesTrack": 200,
#           "cachePagesStore": 100,
#           "cachePagesRefresh": 10,
#           "cachePagesDirtyRead": 10,
#           "searchEngineListTemplate": "forSearchEnginesList.htm",
#           "searchEngineFileTemplate": "forSearchEngines.htm",
#           "searchEngineRobotsDb": "WEB-INF/robots.db",
#           "useDataStore": True,
#           "dataStoreClass": "org.cofax.SqlDataStore",
#           "redirectionClass": "org.cofax.SqlRedirection",
#           "dataStoreName": "cofax",
#           "dataStoreDriver": "com.microsoft.jdbc.sqlserver.SQLServerDriver",
#           "dataStoreUrl": "jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon",
#           "dataStoreUser": "sa",
#           "dataStorePassword": "dataStoreTestQuery",
#           "dataStoreTestQuery": "SET NOCOUNT ON;select test='test';",
#           "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
#           "dataStoreInitConns": 10,
#           "dataStoreMaxConns": 100,
#           "dataStoreConnUsageLimit": 100,
#           "dataStoreLogLevel": "debug",
#           "maxUrlLength": 500}},
#       {
#         "servlet-name": "cofaxEmail",
#         "servlet-class": "org.cofax.cds.EmailServlet",
#         "init-param": {
#           "mailHost": "mail1",
#           "mailHostOverride": "mail2"}},
#       {
#         "servlet-name": "cofaxAdmin",
#         "servlet-class": "org.cofax.cds.AdminServlet"},
#
#       {
#         "servlet-name": "fileServlet",
#         "servlet-class": "org.cofax.cds.FileServlet"},
#       {
#         "servlet-name": "cofaxTools",
#         "servlet-class": "org.cofax.cms.CofaxToolsServlet",
#         "init-param": {
#           "templatePath": "toolstemplates/",
#           "log": 1,
#           "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
#           "logMaxSize": "",
#           "dataLog": 1,
#           "dataLogLocation": "/usr/local/tomcat/logs/dataLog.log",
#           "dataLogMaxSize": "",
#           "removePageCache": "/content/admin/remove?cache=pages&id=",
#           "removeTemplateCache": "/content/admin/remove?cache=templates&id=",
#           "fileTransferFolder": "/usr/local/tomcat/webapps/content/fileTransferFolder",
#           "lookInContext": 1,
#           "adminGroupID": 4,
#           "betaServer": True}}],
#     "servlet-mapping": {
#       "cofaxCDS": "/",
#       "cofaxEmail": "/cofaxutil/aemail/*",
#       "cofaxAdmin": "/admin/*",
#       "fileServlet": "/static/*",
#       "cofaxTools": "/tools/*"},
#
#     "taglib": {
#       "taglib-uri": "cofax.tld",
#       "taglib-location": "/WEB-INF/tlds/cofax.tld"}}}
# ]


l={"1":[[{1:[{2:3},{'x':{2:{2:{2:3}}}}]}]]}

def walk_dict(d, k, v):
  for key,value in d.iteritems():
    if isinstance(value, dict):
      k.append(key)
      walk_dict(d[key], k, v)
    elif isinstance(value, list):
      k.append(key)
      walk_list(value, k, v)
    else:
      k.append(key)
      v.append(value)

def walk_list(lst, k,v):
  for item in lst:
    if isinstance(item, dict):
      walk_dict(item, k, v)
    elif isinstance(item, list):
      walk_list(item, k, v)
    else:
      v.append(item)

key = []
value = []

# data is given in a dict
if isinstance(l, list):
  walk_list(l, key, value)
elif isinstance(l, dict):
  walk_dict(l,key,value)
print("key={0},\n value={1}".format(key, value))

# when data is given as url
url="https://projects.propublica.org/nonprofits/api/v2/search.json?order=revenue&sort_order=desc"
import requests, json
output = requests.get(url)
walk_dict(output.json(),key,value)
print("key={0},\n value={1}".format(key, value))
