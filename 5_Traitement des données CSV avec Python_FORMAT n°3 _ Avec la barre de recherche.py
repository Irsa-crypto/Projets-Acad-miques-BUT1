import csv

def zone2html(csv_filename):
    
    with open(csv_filename, 'r', encoding='utf-8') as file:
        
        reader = csv.DictReader(file, delimiter=';')
        data = list(reader)

    html_content = create_html_table(data)

    with open('FORMAT n°3 _ Avec la barre de recherche.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

def create_html_table(data):
    html_table = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'>
    <style>
    table{
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        margin: 60px auto; 
        color: black;
    }
    th, td {
            border: 1px solid black; 
            padding: 8px; 
            text-align: left; 
        }

    th {
       background-color: #f2f2f2;
       }
    #searchInput {
        margin-top: 20px; 
        padding: 10px;
        font-size: 16px;
        border: 2px solid #3498db; 
        border-radius: 10px;
        outline: none;
    }
    #dataTable {
        margin-top: 20px;
    }
    </style>
    <script>
    function filterTable() {
        var input, filter, table, tr, td, i, valeurs;
        input = document.getElementById("searchInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("dataTable");
        tr = table.getElementsByTagName("tr");

        for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[0]; // On assume que le premier colomn contient la libelle_geographique

            if (td) {
                valeurs = td.textContent || td.innerText;
                if (valeurs.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    }
    </script>
    </head>
    <body>
    <div style="text-align: center;"><h1><br>Professionnels Actifs dans le Domaine Culturel</h1>
                        <h2>Analyse Comparative avec les Effectifs et Professionnels de la Zone</h2> </div>                      
                        <br>
                        <h3><pre><code>Afin de filtrer les données et obtenir des informations spécifiques, veuillez rechercher dans la barre de recherche suivante, le nom de la zone qui vous intéresse : </code></pre></h3>
                        
    <input type="text" id="searchInput" onkeyup="filterTable()" placeholder="Rechercher selon la zone...">
    <table id="dataTable">
    <tr>
        <th>Zone d'emploi</th>
        <th>Nombre total d'actifs</th>
        <th>Nombre actifs de profession culturelle</th>
        <th>Part des professionnels de la culture parmi les actifs</th>
    </tr>
    '''

    for row in data:
    # data c'est "le nombre de lignes qu'il ya dans notre fichier csv".
    #cette boucle va être éxécuter le nombre total de lignes qu'il y a dans la list 'data',
    #et le nombre d'itération sera égal au nombre d'éléments dans la liste 'data' 
        html_table = html_table + f'''<tr> 
                            <td> {row['libelle_geographique']} </td>
                            <td> {row['nombre_total_d_actifs']} </td>
                            <td> {row['nombre_d_actifs_exercant_une_profession_culturelle']} </td>
                            <td> {row['part_des_professionnels_de_la_culture_parmi_les_actifs']} </td>
                          </tr>'''
        #cette boucle précédente va prendre la valeur actuelle de la variable html_table et va y ajouter dans le tableau toutes les données de la ligne correspondente (libelle_geographique....).

    html_table = html_table + '''
    </table>
    </body>
    </html>
    '''

    return html_table

# Utilisation de la fonction avec notre fichier CSV
zone2html("0professions-culturelles_zones-d-emploi_2017_PAR ZONE DEMPLOI.csv")
