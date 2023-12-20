import time
import streamlit as st


st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKnypQIG1DO5YZl8AbdInMzs1W2PrmVst32JqIA0mQGHKyPRgfCitVMQBHBO4XzrQwsWOkWip2Q-9Cwdlohi9AHXxKdrnk7kzL1JyRwNo_1jeQj6ZTA3-DaLsRl9PHwBbCUNtGn-YXqF8jK_-C_shiwuo-cg56rsCEi-LFSJnDwGky57nhJfN7JDHHnMPx/s1794/atas.jpg', caption=None, width=352, use_column_width="never", clamp=False, channels="RGB", output_format="auto")

st.title("Program  Penggajian  PT. AIDA")
st.write("Masukan NIP dan PIN untuk mengecek rincian data gaji anda")

class Karyawan:
    def __init__(self, nip):
        self.nip = nip
def format_rupiah(amount):
    angka = str(amount)
    ribuan = ''
    if len(angka) <= 3:
        return f"Rp. {angka}"
    else:
        while len(angka) > 3:
            ribuan = '.' + angka[-3:] + ribuan
            angka = angka[:-3]
        return f"Rp. {angka}{ribuan}"
    
def cari_data(nip):
    data = {
        19232270112233: {'nama': 'Rifan Fadlan Ramadlan', 'jabatan': 'General Marketing', 'alamat': 'jln. Gobras No 12', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 20 Juni 2003', 'gaji_pokok': 25000000},
        19231901112233: {'nama': 'Ferdi Nuraripin', 'jabatan': 'Regional Sales Manager', 'alamat': 'jln Cibangun no.127', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 08 Mei 2003', 'gaji_pokok': 18000000},
        19231834112233: {'nama': 'Megale Oktana', 'jabatan': 'Sales Manager Marketing', 'alamat': 'jln Manonjaya', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 02 Januari 2003', 'gaji_pokok': 10000000},
        19232453112233: {'nama': 'Hari Fitriana', 'jabatan': 'Supervisor', 'alamat': 'jln Mangkubumi', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 08 Agustus 2002', 'gaji_pokok': 3500000},
        19232521112233: {'nama': 'M. Alif Kudsian Putra', 'jabatan': 'Sales Taking Order', 'alamat': 'Nagarawanagi', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 21 September 2003', 'gaji_pokok': 2700000},
        19231805112233: {'nama': 'Salman Faturrohman', 'jabatan': 'Helper', 'alamat': 'Jakarta', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 29 September 2003', 'gaji_pokok': 2200000},
        19232098112233: {'nama': 'Gilang Sanka', 'jabatan': 'Driver', 'alamat': 'Pangandaran', 'jenis_kelamin': 'Laki-Laki', 'ttl': 'Tasikmalaya, 04 Desember 2002', 'gaji_pokok': 2200000},
    }
    if nip in data:
        return data[nip]
    else:
        return None

def authenticate(nip, pin):
    
    pins = {
        19232270112233: "111111",
        19231901112233: "222222",
        19231834112233: "333333",
        19232453112233: "444444",
        19232521112233: "555555",
        19231805112233: "666666",
        19232098112233: "777777",
    }
    return pins.get(nip) == pin 


    

def main():
    tunjangan_jabatan = {
        'General Marketing': {'tunjangan_jabatan': 3000000, 'tunjangan_makan': 750000},
        'Regional Sales Manager': {'tunjangan_jabatan': 1500000, 'tunjangan_makan': 400000},
        'Sales Manager Marketing': {'tunjangan_jabatan': 700000, 'tunjangan_makan': 200000},
        'Supervisor': {'tunjangan_jabatan': 200000, 'tunjangan_makan': 100000},
        'Sales Taking Order': {'tunjangan_jabatan': 50000, 'tunjangan_makan': 0},
        'Helper': {'tunjangan_jabatan': 0, 'tunjangan_makan': 0},
        'Driver': {'tunjangan_jabatan': 0, 'tunjangan_makan': 0},
    }

    target = {
        'General Marketing': 30000,
        'Regional Sales Manager': 25000,
        'Sales Manager Marketing': 20000,
        'Supervisor': 35000,
        'Sales Taking Order': 50000,
        'Helper': 200,
        'Driver': 1000,
    }

    bonuses = {
        'General Marketing': 10000000,
        'Regional Sales Manager': 6000000,
        'Sales Manager Marketing': 4000000,
        'Supervisor': 2000000,
        'Sales Taking Order': 1500000,
        'Helper': 400000,
        'Driver': 400000,
    }
    
    data_target_per_bulan = {
        'Oktober 2023': {
            'General Marketing': 30200,
            'Regional Sales Manager': 27000,
            'Sales Manager Marketing': 20100,
            'Supervisor': 36000,
            'Sales Taking Order': 50100,
            'Helper': 180,
            'Driver': 1200,
        },
        'November 2023': {
            'General Marketing': 28000,
            'Regional Sales Manager': 24000,
            'Sales Manager Marketing': 20150,
            'Supervisor': 32000,
            'Sales Taking Order': 48000,
            'Helper': 205,
            'Driver': 950,
        },
        'Desember 2023': {
            'General Marketing': 31000,
            'Regional Sales Manager': 25500,
            'Sales Manager Marketing': 18000,
            'Supervisor': 31000,
            'Sales Taking Order': 55000,
            'Helper': 300,
            'Driver': 1350,
        },
    }

    nip_dicari = st.number_input("NIP :", min_value=0, step=1,)
    pin_input = st.text_input("PIN :", type="password")
    st.write("Pilih Bulan/Tahun")
    bulan = st.selectbox("Bulan/Tahun :", ("Oktober 2023", "November 2023", "Desember 2023"))

    if st.button("CARI"):                                       
        with st.status("Memeriksa NIP dan PIN...", expanded=True) as status:
            time.sleep(2)
            st.write("Informasi data...")
            time.sleep(1)
            st.write("Data gaji...")
            time.sleep(1)
            st.write("Unduh data...")
            time.sleep(1)
            status.update(label="jika keterangan 'PIN/NIP salah' silahkan cek kembali NIP dan PIN anda!", state="complete", expanded=True)

        if authenticate(nip_dicari, pin_input):                            
                hasil_pencarian = cari_data(nip_dicari)    
                if hasil_pencarian:
                    nama = hasil_pencarian['nama']
                    jabatan = hasil_pencarian['jabatan']
                    alamat = hasil_pencarian['alamat']
                    jenis_kelamin = hasil_pencarian['jenis_kelamin']
                    ttl = hasil_pencarian['ttl']
                    gaji_pokok = hasil_pencarian['gaji_pokok']

                    tunjangan = tunjangan_jabatan.get(jabatan, {'tunjangan_jabatan': 0, 'tunjangan_makan': 0})
                    gaji_total = gaji_pokok + tunjangan['tunjangan_jabatan'] + tunjangan['tunjangan_makan']

                    st.success(f"Data ditemukan untuk NIP {nip_dicari}")
                    st.markdown(f"**Informasi Data Diri**")
                    st.markdown(f"*Nama: {nama}*")
                    st.markdown(f"*Jabatan: {jabatan}*")
                    st.markdown(f"*Alamat: {alamat}*")
                    st.markdown(f"*Jenis Kelamin : {jenis_kelamin}*")
                    st.markdown(f"*Tempat dan Tanggal Lahir : {ttl}*")

                    gaji_pokok_rupiah = format_rupiah(gaji_pokok)
                    tunjangan_jabatan_rupiah = format_rupiah(tunjangan['tunjangan_jabatan'])
                    tunjangan_makan_rupiah = format_rupiah(tunjangan['tunjangan_makan'])
                
                    st.markdown("**Informasi Detail Gaji**")
                    st.markdown(f"*- Gaji Pokok:  {gaji_pokok_rupiah}*")
                    st.markdown(f"*- Tunjangan Jabatan: {tunjangan_jabatan_rupiah}*")
                    st.markdown(f"*- Tunjangan Makan: {tunjangan_makan_rupiah}*")
                
                    if bulan == "Oktober 2023" or bulan == "November 2023" or bulan == "Desember 2023":

                        if jabatan in target and data_target_per_bulan[bulan][jabatan] >= target[jabatan] :
                            bonus = bonuses[jabatan]
                            st.success(f"+Insentif BONUS! : {format_rupiah(bonus)} karena mencapai target.")
                            st.info(f"*Total Gaji pada bulan {bulan} sebesar {format_rupiah(gaji_total + bonuses.get(jabatan, 0))}*")
                        else:
                            st.warning("Maaf, Anda belum mencapai target untuk mendapatkan bonus.")
                            st.info(f"*Total Gaji pada Bulan {bulan} sebesar {format_rupiah(gaji_total)}*")
                
        else :
            st.error("NIP/PIN salah")
        st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGx5gNLl8rj6SINvpbvZqiaX2cOl9EdvDy-NBvowtaP1AG_oh_NUcolrsc2gDqsrCdUYdmI6GToSSFhUdreAo83svsUGk0kwwDNXffBAJK-u85hlA4SpMK5hsrcY4HBsbzpEsbxM_LwexOk5hXHc6YjLT1HEj_vu8dhODGzGA4sudeLYjoNESfw6KlAuia/s1794/bawah.jpg', caption=None, width=352, use_column_width="never", clamp=False, channels="RGB", output_format="auto")  
if __name__ == "__main__":
    main()