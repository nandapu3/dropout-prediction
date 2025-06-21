# File: mappings.py

# ----------- Binary Mapping -----------
marital_status_map = {
    "Single": 1,
    "Married": 2
}

gender_map = {
    "Female": 0,
    "Male": 1
}

daytime_map = {
    "Evening": 0,
    "Daytime": 1
}

yes_no_map = {
    "Yes": 1,
    "No": 0
}

# ----------- Mother's Qualification -----------
mother_qual_map = {
    "Secondary – 12th yr": 1,
    "Bachelor's": 2,
    "Degree": 3,
    "Master's": 4,
    "Doctorate": 5,
    "Some higher-ed": 6,
    "12th yr – not finished": 9,
    "11th yr – not finished": 10,
    "7th yr (old)": 11,
    "Other 11th yr": 12,
    "10th yr": 14,
    "General commerce": 18,
    "Basic ed 3rd cycle": 19,
    "Tech-professional": 22,
    "7th yr": 26,
    "2nd cycle high-school": 27,
    "9th yr – not finished": 29,
    "8th yr": 30,
    "Unknown": 34,
    "Illiterate": 35,
    "Reads w/o 4th yr": 36,
    "Basic ed 1st cycle": 37,
    "Basic ed 2nd cycle": 38,
    "Tech specialization": 39,
    "HE degree (1st cycle)": 40,
    "Specialized HE": 41,
    "Prof. higher-tech": 42,
    "HE master (2nd)": 43,
    "HE doctorate (3rd)": 44
}

# ----------- Father's Qualification -----------
father_qual_map = mother_qual_map.copy()  # atau bisa ditambah variasinya jika ada

# ----------- Mother's Occupation -----------
mother_occ_map = {
    "Student": 0,
    "Executives / Managers": 1,
    "Intellectual & Scientific": 2,
    "Technician / Associate": 3,
    "Administrative": 4,
    "Services / Sales": 5,
    "Farmer / Forestry": 6,
    "Skilled Industry / Craft": 7,
    "Machine Operator": 8,
    "Unskilled": 9,
    "Armed Forces": 10,
    "Other / Blank": 90,
    "Health professionals": 122,
    "Teachers": 123,
    "ICT Specialists": 125,
    "Legal/Social Technicians": 134
    # Tambahkan sesuai kebutuhan
}

# ----------- Father's Occupation -----------
father_occ_map = {
    "Student": 0,
    "Executives / Managers": 1,
    "Intellectual & Scientific": 2,
    "Technician / Associate": 3,
    "Administrative": 4,
    "Services / Sales": 5,
    "Farmer / Forestry": 6,
    "Skilled Industry / Craft": 7,
    "Machine Operator": 8,
    "Unskilled": 9,
    "Armed Forces": 10,
    "Other / Blank": 90,
    "Health professionals": 122,
    "Teachers": 123,
    "ICT Specialists": 125,
    "Legal/Social Technicians": 134,
    "Electricians / Technicians": 174,
    "Food Industry Workers": 175,
    "Vehicle Operators": 183,
    "Construction Workers": 171,
    "Administrative Support": 144
    # Tambahkan entri lain sesuai kebutuhan
}
