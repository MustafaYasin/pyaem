import pyaem
print(PyAem)
aem = pyaem.PyAem('admin', 'admin','unil-author.corp.adobe.com', 80)

aem.create_package('test_mustafa_2', 'bag', '2.0')