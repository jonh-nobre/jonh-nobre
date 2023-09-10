import pygal

pie = pygal.Pie()
pie.title = "TEMPO GASTO NAS REDES SOCIAIS"
pie.add("Twitter", 12)
pie.add("WhatsApp", 35)
pie.add("Facebook", 23)
pie.add("Instagram", 30)

pie.render_in_browser()