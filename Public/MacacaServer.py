import os
import requests

from multiprocessing import Pool


class MacacaServer:
    def __init__(self, runs):
        self._runs = runs
        self._cmd = 'macaca server -p %s --verbose'
        self._url = 'http://127.0.0.1:%s/wd/hub/status'

    @staticmethod
    def server_url(port):
        server_url = {
            'hostname': '127.0.0.1',
            'port': port,
        }

        return server_url

    def start_server(self):
        pool = Pool(processes=len(self._runs))

        for run in self._runs:
            pool.apply_async(self._run_server, args=(run,))

        pool.close()

        # after start macaca server, macaca server process can not return, so should not join
        # p.join()

    def _run_server(self, run):
        port = run.get_port()
        cmd = str(self._cmd + ' > ' + run.get_path() + '\\' + 'macaca_server_port_%s.log') % (port, port)
        os.system(cmd)

    def is_running(self, port):
        url = self._url % port

        response = None
        try:
            response = requests.get(url, timeout=0.1)

            if str(response.status_code).startswith('2'):
                # data = json.loads((response.content).decode("utf-8"))
                # if data.get("staus") == 0:
                return True

            return False
        except requests.exceptions.ConnectionError:
            return False
        except requests.exceptions.ReadTimeout:
            return False
        finally:
            if response:
                response.close()


