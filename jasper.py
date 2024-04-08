import os
from pyreportjasper import PyReportJasper

reports_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "reports")
resources_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources")
output_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "output")
input_file_jrxml = os.path.join(reports_dir, "teste.jrxml")
input_file_jasper = os.path.join(reports_dir, "teste.jasper")
resource_json = os.path.join(resources_dir, "teste.json")
output_file = os.path.join(output_dir, "teste")


# compila o .JRXML e trasnforma em .jasper
def compiling():
    pyreportjasper = PyReportJasper()
    pyreportjasper.config(input_file=input_file_jrxml)
    pyreportjasper.compile(write_jasper=True)


# processa o .jrxml e gera o PDF
def processing():
    pyreportjasper = PyReportJasper()
    pyreportjasper.config(
        input_file=input_file_jasper, output_file=output_file, output_formats=["pdf"]
    )
    pyreportjasper.process_report()


# processa o .jrxml e gera o PDF com conexão JSON
def json_to_pdf():
    conn = {"driver": "json", "data_file": resource_json, "json_query": "USER"}
    pyreportjasper = PyReportJasper()
    pyreportjasper.config(
        input_file=input_file_jasper,
        output_file=output_file,
        output_formats=["pdf"],
        db_connection=conn,
    )

    pyreportjasper.process_report()
    print("Result is the file below.")
    print(output_file + ".pdf")


# compiling()
# processing()
json_to_pdf()
