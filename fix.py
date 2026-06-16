import sys

with open('/Users/alessiomariani/siti_web/mister_up_new_v2/misterSelf.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content = """        <section class="section bg-dark-3">
            <div class="container mb40">

                <div class="row row-50 justify-content-center justify-content-lg-between align-items-center">

                    <!-- VIDEO -->
                    <div class="col-md-10 col-lg-6 wow-outer">
                        <div class="thumbnail-video-1 bg-dark-1 wow slideInRight">
                            <div class="embed-responsive embed-responsive-16by9">
                                <iframe
                                        width="560"
                                        height="315"
                                        src="https://www.youtube.com/embed/QZzbm-FrkGk?rel=0&showinfo=0"
                                        title="Video dimostrativo"
                                        frameborder="0"
                                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                        allowfullscreen>
                                </iframe>
                            </div>
                        </div>
                    </div>

                    <!-- CAROSELLO CARATTERISTICHE -->
                    <div class="col-md-10 col-lg-5 wow-outer carosello-caratteristiche">

                        <div class="owl-carousel owl-checklist wow slideInLeft"
                             data-items="1"
                             data-dots="false"
                             data-nav="false"
                             data-loop="true"
                             data-margin="30"
                             data-stage-padding="0"
                             data-mouse-drag="true"
                             data-autoplay="false">

                            <!-- SLIDE 1: Monete -->
                            <div class="checklist">
                                <h4 class="mb-2">Riciclatore di monete</h4>
                                <p class="checklist-subtitle mb-3">
                                    <b>Innovative Technology - SMART Coin System</b>
                                </p>
                                <div class="m4-specs-grid">
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in accettazione/erogazione: 0,02 € - 0,05 € - 0,10 € - 0,20 € - 0,50 € - 1,00 € - 2,00 € (configurabili)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità monete riciclo: 2000 pz totali</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità monete cassetto: 700 pz</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Modalità accettazione/erogazione: monete multiple</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Velocità accettazione/erogazione: 12 monete/secondo</p>
                                    </div>
                                </div>
                            </div>

                            <!-- SLIDE 2: Banconote CPI/MEI -->
                            <div class="checklist">
                                <h4 class="mb-2">Riciclatore di banconote</h4>
                                <p class="checklist-subtitle mb-3">
                                    <b>CPI/MEI - BNR Advance 320:</b>
                                </p>
                                <div class="m4-specs-grid">
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in accettazione: 5,00 € - 10,00 € - 20,00 € - 50,00 € - 100,00 € - 200,00 € - 500,00 €</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in erogazione: n° 4 tagli in riciclo configurabili (predefiniti 5,00 € - 10,00 € - 20,00 € - 50,00 €)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità banconote riciclo: 180 pz totali (60 pz per due tagli e 30 pz per gli altri due tagli; configurabili)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità banconote cassetto: 600 pz</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Modalità erogazione: mazzetta (fino a 15 banconote insieme)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Velocità accettazione/erogazione: 3 banconote/secondo</p>
                                    </div>
                                </div>
                            </div>

                            <!-- SLIDE 3: JCM -->
                            <div class="checklist">
                                <h4 class="mb-2">Riciclatore di banconote</h4>
                                <p class="checklist-subtitle mb-3">
                                    <b>JCM – UBA ProRQ:</b>
                                </p>
                                <div class="m4-specs-grid">
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in accettazione: 5,00 € - 10,00 € - 20,00 € - 50,00 € - 100,00 € - 200,00 € - 500,00 €</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in erogazione: n° 4 tagli in riciclo configurabili (predefiniti 5,00 € - 10,00 € - 20,00 € - 50,00 €)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità banconote riciclo: 180 pz totali (60 pz per ogni taglio)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità banconote cassetto: 400 pz</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Modalità accettazione/erogazione: singola banconota</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Velocità accettazione/erogazione: 2 banconote/secondo</p>
                                    </div>
                                </div>
                            </div>

                            <!-- SLIDE 4: GRG -->
                            <div class="checklist">
                                <h4 class="mb-2">Riciclatore di banconote</h4>
                                <p class="checklist-subtitle mb-3">
                                    <b>GRG BR-15:</b>
                                </p>
                                <div class="m4-specs-grid">
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in accettazione: 5,00 € - 10,00 € - 20,00 € - 50,00 € - 100,00 € - 200,00 € - 500,00 €</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in erogazione: n° 4 tagli in riciclo configurabili (predefiniti 5,00 € - 10,00 € - 20,00 € - 50,00 €)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità banconote riciclo: 80 pz per due tagli e 50 pz per gli altri due (configurabili)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità banconote cassetto: 1000 pz</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Modalità erogazione: mazzetta (fino a 15 banconote insieme)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Velocità accettazione/erogazione: 3 banconote/secondo</p>
                                    </div>
                                </div>
                            </div>

                            <!-- SLIDE 5: SPECTRAL -->
                            <div class="checklist">
                                <h4 class="mb-2">Riciclatore di banconote</h4>
                                <p class="checklist-subtitle mb-3">
                                    <b>Innovative Technology - SPECTRAL Payout:</b>
                                </p>
                                <div class="m4-specs-grid">
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in accettazione: 5,00 € - 10,00 € - 20,00 € - 50,00 € - 100,00 € - 200,00 € - 500,00 €</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Tagli in erogazione: n° 4 tagli in riciclo configurabili (predefiniti 5,00 € - 10,00 € - 20,00 € - 50,00 €)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità banconote riciclo: 80 pz totali</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Capacità banconote cassetto: 500 pz o 1000 pz (opzionale)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Modalità accettazione/erogazione: singola banconota</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Velocità accettazione/erogazione: 1 banconota/secondo</p>
                                    </div>
                                </div>
                            </div>

                            <!-- SLIDE 6: POS -->
                            <div class="checklist checklist-fixed">
                                <h4 class="mb-2">Terminale POS(opzionale)</h4>
                                <p class="checklist-subtitle mb-3">
                                    <b>PAX IM20</b>
                                </p>
                                <div class="m4-specs-grid">
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Pagamento elettronico tramite Carte di Debito, Credito e Prepagate</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Pagamento Contact-Less o Contact-Chip (a discrezione del cliente)</p>
                                    </div>
                                    <div class="m4-spec-card">
                                        <span class="check-icon linearicons-check"></span>
                                        <p>Display touchscreen a colori (per istruzioni e digitazione PIN)</p>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <div class="owl-3dots">
                            <span class="dot-prev">&#8592;</span>
                            <span class="dot-center"></span>
                            <span class="dot-next">&#8594;</span>
                        </div>
                    </div>

                </div>
            </div>
        </section>
"""
lines[286:404] = [new_content]

with open('/Users/alessiomariani/siti_web/mister_up_new_v2/misterSelf.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

