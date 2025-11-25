import axios from "axios";

const SERVICE1 = "http://127.0.0.1:8000/api";
const SERVICE2 = "http://127.0.0.1:8001/api";

// -------- Service 1: Alunos --------
export async function getAlunos() {
  const res = await axios.get(`${SERVICE1}/alunos/`);
  return res.data;
}

export async function createAluno(data) {
  const res = await axios.post(`${SERVICE1}/alunos/`, data);
  return res.data;
}

export async function updateAluno(id, data) {
  const res = await axios.put(`${SERVICE1}/alunos/${id}/`, data);
  return res.data;
}

export async function deleteAluno(id) {
  await axios.delete(`${SERVICE1}/alunos/${id}/`);
}

// -------- Service 1: Matrículas (ex.: só GET/POST) --------
export async function getMatriculas() {
  const res = await axios.get(`${SERVICE1}/matriculas/`);
  return res.data;
}

export async function createMatricula(data) {
  const res = await axios.post(`${SERVICE1}/matriculas/`, data);
  return res.data;
}

// -------- Service 2: Notas --------
export async function getNotas() {
  const res = await axios.get(`${SERVICE2}/notas/`);
  return res.data;
}

export async function createNota(data) {
  const res = await axios.post(`${SERVICE2}/notas/`, data);
  return res.data;
}

export async function updateNota(id, data) {
  const res = await axios.put(`${SERVICE2}/notas/${id}/`, data);
  return res.data;
}

export async function deleteNota(id) {
  await axios.delete(`${SERVICE2}/notas/${id}/`);
}
