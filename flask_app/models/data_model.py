import pandas as pd
import io

class DataModel:
    def __init__(self):
        self.df = None

    def load_csv(self, file):
        try:
            df = pd.read_csv(file)

            if df.empty:
                return "<b>Error:</b> El archivo CSV está vacío o no contiene registros."

            if df.columns.size == 0:
                return "<b>Error:</b> El archivo CSV no tiene columnas válidas."

            self.df = df
            return "<b>Archivo cargado correctamente.</b>"

        except pd.errors.EmptyDataError:
            return "<b>Error:</b> El archivo CSV está completamente vacío."
        except pd.errors.ParserError:
            return "<b>Error:</b> El archivo CSV tiene un formato incorrecto o está dañado."
        except Exception as e:
            return f"<b>Error:</b> No se pudo cargar el archivo: {str(e)}"

    def _check_loaded(self):
        if self.df is None:
            return False, "<b>Error:</b> No se ha cargado ningún archivo CSV."
        return True, None

    def get_head(self, n):
        ok, msg = self._check_loaded()
        if not ok:
            return msg
        return self.df.head(n).to_html()

    def get_tail(self, n):
        ok, msg = self._check_loaded()
        if not ok:
            return msg
        return self.df.tail(n).to_html()

    def get_info(self):
        ok, msg = self._check_loaded()
        if not ok:
            return msg
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        return buffer.getvalue().replace('\n', '<br>')

    def get_columns(self):
        ok, msg = self._check_loaded()
        if not ok:
            return msg
        return self.df.columns.tolist()

    def get_shape(self):
        ok, msg = self._check_loaded()
        if not ok:
            return msg
        return str(self.df.shape)

    def get_describe(self):
        ok, msg = self._check_loaded()
        if not ok:
            return msg
        return self.df.describe().to_html()

    def select_column(self, col):
        ok, msg = self._check_loaded()
        if not ok:
            return msg
        try:
            return self.df[[col]].to_html()
        except KeyError:
            return f"<b>Error:</b> La columna '{col}' no existe en el archivo."

    def select_columns(self, cols):
        ok, msg = self._check_loaded()
        if not ok:
            return msg
        try:
            return self.df[cols].to_html()
        except KeyError as e:
            missing = [c for c in cols if c not in self.df.columns]
            return f"<b>Error:</b> Las siguientes columnas no existen: {', '.join(missing)}"

    def filter_rows(self, col, op, val):
        ok, msg = self._check_loaded()
        if not ok:
            return msg

        if col not in self.df.columns:
            return f"<b>Error:</b> La columna '{col}' no existe."

        try:
            if op == '==':
                result = self.df[self.df[col] == val]
            elif op == '<':
                result = self.df[self.df[col] <= float(val)]
            elif op == '>':
                result = self.df[self.df[col] >= float(val)]
            else:
                return "<b>Error:</b> Operador no válido. Use <, > o ==."

            return result.to_html()
        except ValueError:
            return "<b>Error:</b> No se pudo interpretar el valor. Asegúrese de que sea numérico para operaciones < o >, o texto exacto para ==."
        except Exception as e:
            return f"<b>Error:</b> {str(e)}"
