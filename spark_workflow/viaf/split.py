import xml.etree.ElementTree as ET
import json
import unicodedata
from unidecode import unidecode


ns = {'xmlns': 'http://viaf.org/viaf/terms#'}

output_name = "outputDataSet_4_15"
input_name = "viaf-20160321-clusters.xml"

# input_name = "data2"
# input_name = "output"
# output_name = "outputDataSet_test"


with open(output_name, 'w') as fout:
	with open(input_name, "r") as fin:
		for line in fin:
			xml = line.split("\t")[1]
			# print xml 
			root = ET.fromstring(xml)
			# print root.tag
			# for child in root:
			# 	print child.tag, child.attrib
			if root.find('xmlns:nameType', ns).text=="Personal":
				dict_person = {}
				list_names = []
				list_additionalSources = []
				
				#For ID
				dict_person['@id'] = "http://viaf.org/viaf/" + root.find('xmlns:viafID', ns).text

				#For Type
				dict_person["@type"] = "http://schema.org/Person"

				# For Name
				dict_person['schema:name'] = unidecode(root.find('xmlns:mainHeadings', ns).find('xmlns:data', ns).find('xmlns:text', ns).text)
				
				# For BirthDate
				birthDate = root.find('xmlns:birthDate', ns).text
				if birthDate != "0":
					dict_person['schema:birthDate'] = birthDate

				# For DeathDate
				deathDate = root.find('xmlns:deathDate', ns).text
				if deathDate != "0":
					dict_person['schema:deathDate'] = deathDate

				# For gender
				try:
					gender = root.find('xmlns:fixed', ns).find('xmlns:gender', ns).text
					if gender == "a":
						dict_json["schema:gender"] = "Female"
					elif gender == "b":
						dict_json["schema:gender"] = "Male"
				except:
					pass
				
				# For Nationality
				try:
					dict_person['schema:nationality'] = root.find('xmlns:nationalityOfEntity', ns).find('xmlns:data', ns).find('xmlns:text', ns).text
				except:
					pass

				# For Additional names
				mainHeadingEls = root.find('xmlns:mainHeadings', ns).findall('xmlns:mainHeadingEl', ns)
				for mainHeadingEl in mainHeadingEls:
					# Concate last name and first name
					subfields = mainHeadingEl.find('xmlns:datafield', ns).findall('xmlns:subfield', ns)
					first_name = ""
					last_name = ""
					for subfield in subfields:
						if subfield.get('code')=="a":
							last_name = subfield.text
						elif subfield.get('code')=="b":
							first_name = subfield.text
					name = unidecode((last_name + " " + first_name).strip())
					if name not in list_names and name!=dict_person['schema:name']:
						list_names.append(name)

					# Get source id
					dict_additionalSource = {}
					sourceID = mainHeadingEl.find('xmlns:id', ns).text
					if sourceID:
						source_name, source_id = sourceID.split("|")
						dict_additionalSource["ID"] = source_id
						dict_additionalSource["source"] = source_name
						dict_additionalSource["name"] = name
						list_additionalSources.append(dict_additionalSource)

				if list_names:
					dict_person['schema:additionalName'] = list_names

				if list_additionalSources:
					dict_person['additionalSource'] = list_additionalSources
				
				#write to files
				# json_str = json.dumps(dict_person, ensure_ascii=False).encode("utf8")
				json_str = json.dumps(dict_person)

				# print json_str
				fout.write(json_str + "\n")
