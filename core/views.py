import io
from django.http import FileResponse
from django.views.generic import View

from reportlab.pdfgen import canvas

###weasyprint
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse

from weasyprint import HTML

class IndexView(View):

        def get(self, request, *args, **kwargs):
            #crição do arquivo
            buffer = io.BytesIO()

            #criar arquivos pdf
            pdf = canvas.Canvas(buffer)

            #inserção de coisas no pdf
            pdf.drawString(100, 100, "Matheus Mozart")

            #execução de métodos
            pdf.showPage()
            pdf.save()

            #terminado, volta para o ínício
            buffer.seek(0)
            #FAZ O DAWLOAND AO ABRIR A PÁGINA
            #return FileResponse(buffer, as_attachment=True, filename='relatorio.pdf')

            #MOSTRA DIRETO NO NAVEGADOR
            return FileResponse(buffer, filename='relatorio.pdf')


class Index2View(View):

    def get(self, request, *args, **kwargs):
        texto = ['Matheus Mozart dev', 'Eu sou fodda, vou conseguir e serei progamador web com tudo, pois consigo aprender']

        html_string = render_to_string('relatorio.html', {'texto': texto})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/relatorio2.pdf')

        fs = FileSystemStorage('/temp')

        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # Faz o download do arquivo PDF direto
            # response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf"'
            # Abre o PDF direto no navegador
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'
        return response
