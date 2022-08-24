
from pdf2image import convert_from_path

for f in range(1,12):
    if f == 4 or f == 5:
        pass
    else:
        pages = convert_from_path('assets/img/certficatepdf/cert'+str(f)+'.pdf')
        print("Converting", f, "file ...",'./assets/certficates/certificate'+str(f)+'.pdf')

        for i in range(len(pages)):
            pages[i].save('assets/img/certficates/cert'+ str(f) +'.jpg', 'JPEG')
            print("Converted", f, "file ...")