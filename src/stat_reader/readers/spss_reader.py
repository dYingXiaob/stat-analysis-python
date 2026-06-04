import pyreadstat

def load_spss(path):
    df, meta = pyreadstat.read_sav(path)
    return df, meta