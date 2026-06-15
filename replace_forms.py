import glob
import re

files = glob.glob('site/*.html')

pattern = re.compile(r'<form class="rd-form rd-mailform">.*?</form>', re.DOTALL)

replacement = """<form class="rd-form rd-mailform" data-form-output="form-output-global" data-form-type="contact" method="post" action="bat/rd-mailform.php">
  <div class="row">
    <div class="col-md-6 mb-3"><input class="form-input" type="text" name="name" placeholder="Nome" data-constraints="@Required"></div>
    <div class="col-md-6 mb-3"><input class="form-input" type="text" name="surname" placeholder="Cognome" data-constraints="@Required"></div>
    <div class="col-md-6 mb-3"><input class="form-input" type="email" name="email" placeholder="Email" data-constraints="@Email @Required"></div>
    <div class="col-md-6 mb-3"><input class="form-input" type="text" name="phone" placeholder="Telefono" data-constraints="@Numeric @Required"></div>
    <div class="col-md-6 mb-3"><input class="form-input" type="text" name="activity" placeholder="Tipo di attività"></div>
    <div class="col-md-6 mb-3"><input class="form-input" type="text" name="model" placeholder="Modello dispositivo/interesse"></div>
    <div class="col-12 mb-3"><textarea class="form-input" name="message" rows="4" placeholder="Messaggio o richiesta..." data-constraints="@Required"></textarea></div>
  </div>
  <button class="button button-primary w-100" type="submit">Invia richiesta</button>
</form>"""

for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    if '<form class="rd-form rd-mailform">' in content:
        # We need to maintain indentation if possible, but let's just replace it.
        # The form is already replaced in contatti.html, so it won't match.
        new_content = pattern.sub(replacement, content)
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Updated {file}")

