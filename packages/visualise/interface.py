def generate_interface(html_files):
    # Generate div containers and buttons for each HTML file
    # Button CSS taken from https://getcssscan.com/css-buttons-examples

    divs = ""
    buttons = ""
    for i, file in enumerate(html_files):
        with open(file, "r") as f:
            file_content = f.read()
            div_id = f"div-{i+1}"
            div = f'<div class="plot-div active" id="{div_id}">{file_content}</div>'
            divs += div

            button = f'<button class="button-9" onclick="showDiv(\'{div_id}\')">{file.split("/")[-1].replace(".html", "")}</button>'
            buttons += button

    # Create the main HTML page
    page_content = f'''
    <html>
        <head>
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                }}
                #button-bar {{
                    display: flex;
                    justify-content: flex-start;
                    align-items: center;
                    background-color: #f2f2f2;
                    height: 10%;
                }}
                button {{
                    margin: 5px;
                }}
                .button-9 {{
                    appearance: button;
                    backface-visibility: hidden;
                    background-color: #405cf5;
                    border-radius: 6px;
                    border-width: 0;
                    box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;
                    box-sizing: border-box;
                    color: #fff;
                    cursor: pointer;
                    font-family: -apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue",Ubuntu,sans-serif;
                    font-size: 100%;
                    height: 44px;
                    line-height: 1.15;
                    outline: none;
                    overflow: hidden;
                    padding: 0 25px;
                    position: relative;
                    text-align: center;
                    text-transform: none;
                    transform: translateZ(0);
                    transition: all .2s,box-shadow .08s ease-in;
                    user-select: none;
                    -webkit-user-select: none;
                    touch-action: manipulation;
                    width: 100%;
                }}

                .button-9:disabled {{
                    cursor: default;
                }}

                .button-9:focus {{
                    box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset, rgba(50, 50, 93, .2) 0 6px 15px 0, rgba(0, 0, 0, .1) 0 2px 2px 0, rgba(50, 151, 211, .3) 0 0 0 4px;
                }}
                .plot-div {{
                    width: 100%;
                    height: 90%;
                    border: none;
                    display: none;
                }}
                .plot-div.active {{
                    display: block;
                }}
            </style>
            <script>
                function showDiv(divId) {{
                    var divs = document.getElementsByClassName('plot-div');
                    for (var i = 0; i < divs.length; i++) {{
                        divs[i].classList.remove('active');
                    }}
                    var selectedDiv = document.getElementById(divId);
                    selectedDiv.classList.add('active');
                }}
                window.onload = function() {{
                    showDiv('div-1');
                    }};
            </script>
        </head>
        <body>
            <div id="button-bar">
                {buttons}
            </div>
            <div id="plot-container">
                {divs}
            </div>
        </body>
    </html>
    '''

    # Write the HTML page to a file
    with open("/result/viewer.html", "w") as f:
        f.write(page_content)
