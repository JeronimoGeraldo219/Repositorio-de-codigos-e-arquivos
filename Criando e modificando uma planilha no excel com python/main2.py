import openpyxl
# Escolhendo o arquivo para ler
book = openpyxl.load_workbook('Planilha dos físicos.xlsx')

#Escolhendo a página do arquivo que você quer ler
Physics_page = book['Physics']

#Mostrando os dados das linhas
for rows in Physics_page.iter_rows(min_row = 2):

    #Imprimindo as linhas
    #print(rows[0].value,rows[1].value,rows[2].value) 
    
    
    
    #imprimindo a partir das células
     for cell in rows:
       print(cell.value)
