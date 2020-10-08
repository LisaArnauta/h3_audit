import requests

class Getter:
    def __init__(self):
        pass

    def work(self,url_list):
        '''

        :return: list(dict(url, status_code,html))
        '''
        result = self._get_html(url_list)
        return result


    def _get_html(self,url_list):
        '''

        :return: dict(url, status_code, html)
        '''
        result = list()
        session = requests.Session()
        # TODO :consider implementing UA generator
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/83.0.4103.116 Safari/537.36'}
        for url in self.url_list:
            custom_status = None
            try:
                response = session.get(self.url, headers=headers)
            except requests.exceptions.ConnectionError as e:
                status = 1001
            except requests.exceptions.Timeout as e:
                status = 1002
            except Exception as e:
                custom_status = 1013
            finally:
                url_result = {
                    'url': url,
                    'status_code': custom_status if custom_status
                    else response.status_code,
                    'html': '' if custom_status else response.text
                }
                result.append(url_result)



if __name__ == '__main__':
    url_list = []
    getter = Getter(url_list)
    res = getter.work()
    print(res)