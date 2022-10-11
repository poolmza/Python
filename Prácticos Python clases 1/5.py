
pph = int(625)
hts = int(input("Horas trabajadas por semana: "))
htps = (pph*hts*4)
htpsx = (((pph*1.5*4)*(hts-40))+(625*160))

if (hts <= 40):
    print ("Sueldo por mes: ", htps)
if (hts > 40):
    print ("sueldo mensual: ", htpsx)