const express = require("express");

const app = express();
const ip = "0.0.0.0";
const port = 4000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/jasonrizki", (req, res) => {
  res.json([
    {
      nama: "Jasson Franklyn Wang",
      nim: "L0122081",
    },
    {
      nama: "Mohammad Rizki Maulana",
      nim: "L0122096",
    },
  ]);
});

let mahasiswa = [];

app.get("/mahasiswa", (req, res) => {
  res.json(mahasiswa);
});

app.post("/mahasiswa", (req, res) => {
  const { nama, nim } = req.body;

  if (!nama || !nim) {
    return res.status(400).json({ error: "Nama dan NIM harus diisi!" });
  }

  mahasiswa.push({ nama, nim });
  res
    .status(201)
    .json({ message: "Mahasiswa berhasil ditambahkan", data: { nama, nim } });
});

app.listen(port, ip, () => {
  console.log(`server berjalan di http://${ip}:${port}`);
});
