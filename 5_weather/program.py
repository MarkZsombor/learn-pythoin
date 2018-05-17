import requests

def main():
  print_header()
  area_code = input('What zipcode do you want the weather for?')
  html = get_html_from_web(area_code)
  # parse html
  # display forecast


def print_header():
  print('Weather App')

def get_html_from_web(zip_code):
  url = 'http://www.wunderground.com/weather/{}'.format(zip_code)
  response = requests.get(url)
  # print(url)
  # print(response.text[0:250])
  return response.text

if __name__ == '__main__':
  main()