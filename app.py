from flask import Flask, render_template, request, flash

app = Flask(__name__)
#app.secret_key = 'b18c5212951a96d2653dab889f2844c4ca0b9ad5c19d1f92'
#app.config['SECRET_CATEGORY'] = 'message'


#@app.route('/')
#def home():

#    return render_template('new_home.html')
messages = []

@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        jobID = request.form['jobID']
        fasta = request.form['fasta']

        if not fasta:
            #flash('sequences are required')
            pass
        else:
            messages.append({'title': jobID, 'content': fasta})
            return(render_template('new_home.html'))

    return render_template('real_home.html')


## TO DO
'''
Python pieces
1. need fasta functions to unpack what user put in messages
2. need MSA function
3. need ESMfold calls ------------------------------------

sequence = st.text_input(label="Protein Sequence", value=suggestion)

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
name = sequence[:3] + sequence[-3:]
pdb_string = response.content.decode('utf-8')

4. need to plot pdbs ----------------------------------

xyzview = py3Dmol.view()
xyzview.addModel(pdb_string, 'pdb')
xyzview.setStyle({'cartoon': {
    "color": "spectrum", }})
xyzview.zoomTo()
print("Set style")
showmol(xyzview, height=500, width=800)

#######################################################

HTML & CSS pieces
1. populate MSA window with MSA
2. 
'''






## This is the code to access ESMfold
#suggestion = 'ANYPEPTIDECANFILLTHISSPACE  # grab first sequence
#sequence = st.text_input(label="Protein Sequence", value=suggestion)

#headers = {
#    'Content-Type': 'application/x-www-form-urlencoded'
#}

#response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)

if __name__ == '__main__':
    app.run()
