import streamlit as st 
from datetime import datetime

# Titel der Anwendung
st.title("Stromverbrauchsrechner")

# Benutzereingaben
begin_date = st.date_input("Geben Sie das Begin Datum ein:", value=None)
between_date = st.date_input("Geben Sie das  Preisanpassungs Datum ein:", value=None)
end_date = st.date_input("Geben Sie das End Datum ein:", value=None)
total_kwh = st.number_input("Geben Sie den gesamten Stromverbrauch in kWh für den gesamten Zeitraum ein:", min_value=0.0, format="%.2f")

# Berechnungs-Button
if st.button("Berechnen"):

    if not begin_date or not between_date or not end_date:
        st.error("Bitte geben Sie die Daten im richtigen Format ein (TT/MM/JJJJ).")
    else:
        total_days = (end_date - begin_date).days + 1
        days_begin_to_between = (between_date - begin_date).days
        days_between_to_end = (end_date - between_date).days + 1

        if total_days <= 0 or days_begin_to_between < 0 or days_between_to_end < 0:
            st.error("Ungültiger Datumsbereich. Stellen Sie sicher, dass die Daten in chronologischer Reihenfolge eingegeben sind.")
        else:
            consumption_per_day = total_kwh / total_days
            consumption_begin_to_between = consumption_per_day * days_begin_to_between
            consumption_between_to_end = consumption_per_day * days_between_to_end

            st.success(f"Gesamtanzahl der Tage: {total_days} Tage")
            st.write(f"Verbrauch pro Tag: {consumption_per_day:.2f} kWh")

            st.markdown("---")
            st.write(f"Von {begin_date} bis {between_date} (letzter Tag ausgeschlossen): {days_begin_to_between} Tage")
            st.write(f"Verbrauch: {consumption_begin_to_between:.2f} kWh")

            st.markdown("---")
            st.write(f"Von {between_date} bis {end_date} (letzter Tag eingeschlossen): {days_between_to_end} Tage")
            st.write(f"Verbrauch: {consumption_between_to_end:.2f} kWh")
