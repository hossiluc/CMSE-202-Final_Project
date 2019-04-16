w = widgets.Dropdown(               #creates a dropdown menu with the data keys from the dictionary above as options
    options=mydata.keys(),
    value = default,
    description='Data',)