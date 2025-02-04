from bs4 import BeautifulSoup


def extract_city_names(file_path):
    """
    Extracts all city names from the provided HTML file.

    Parameters:
        file_path (str): Path to the HTML file.

    Returns:
        list: A list of city names.
    """
    # Open the HTML file and parse it with BeautifulSoup
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    city_names = []

    # Loop through all rows in the table
    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if columns:  # Skip rows without table data cells
            city_name = columns[0].get_text(strip=True)
            city_names.append(city_name)

    return city_names
