import { useEffect, useState } from "react";
import {
  getAlunos,
  createAluno,
  updateAluno,
  deleteAluno,
  getNotas,
  createNota,
  updateNota,
  deleteNota,
} from "./api";

function App() {
  // ------ STATE ALUNOS ------
  const [alunos, setAlunos] = useState([]);
  const [alunoForm, setAlunoForm] = useState({
    id: null,
    nome: "",
    email: "",
    idade: "",
  });

  // ------ STATE NOTAS ------
  const [notas, setNotas] = useState([]);
  const [notaForm, setNotaForm] = useState({
    id: null,
    aluno_id: "",
    curso_id: "",
    valor: "",
  });

  // Carrega dados ao abrir
  useEffect(() => {
    carregarAlunos();
    carregarNotas();
  }, []);

  async function carregarAlunos() {
    const data = await getAlunos();
    setAlunos(data);
  }

  async function carregarNotas() {
    const data = await getNotas();
    setNotas(data);
  }

  // --------- HANDLERS ALUNO ---------
  function handleAlunoChange(e) {
    const { name, value } = e.target;
    setAlunoForm((prev) => ({ ...prev, [name]: value }));
  }

  async function handleAlunoSubmit(e) {
    e.preventDefault();
    const payload = {
      nome: alunoForm.nome,
      email: alunoForm.email,
      idade: Number(alunoForm.idade),
    };

    if (alunoForm.id) {
      await updateAluno(alunoForm.id, payload); // PUT
    } else {
      await createAluno(payload); // POST
    }

    setAlunoForm({ id: null, nome: "", email: "", idade: "" });
    await carregarAlunos();
  }

  function handleAlunoEdit(aluno) {
    setAlunoForm({
      id: aluno.id,
      nome: aluno.nome,
      email: aluno.email,
      idade: aluno.idade,
    });
  }

  async function handleAlunoDelete(id) {
    await deleteAluno(id); // DELETE
    await carregarAlunos();
  }

  // --------- HANDLERS NOTA ---------
  function handleNotaChange(e) {
    const { name, value } = e.target;
    setNotaForm((prev) => ({ ...prev, [name]: value }));
  }

  async function handleNotaSubmit(e) {
    e.preventDefault();
    const payload = {
      aluno_id: Number(notaForm.aluno_id),
      curso_id: Number(notaForm.curso_id),
      valor: Number(notaForm.valor),
    };

    if (notaForm.id) {
      await updateNota(notaForm.id, payload); // PUT
    } else {
      await createNota(payload); // POST
    }

    setNotaForm({ id: null, aluno_id: "", curso_id: "", valor: "" });
    await carregarNotas();
  }

  function handleNotaEdit(nota) {
    setNotaForm({
      id: nota.id,
      aluno_id: nota.aluno_id,
      curso_id: nota.curso_id,
      valor: nota.valor,
    });
  }

  async function handleNotaDelete(id) {
    await deleteNota(id); // DELETE
    await carregarNotas();
  }

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>Dashboard Acadêmico</h1>

      {/* ---------- ALUNOS ---------- */}
      <section style={{ marginBottom: "2rem" }}>
        <h2>Alunos (Service 1)</h2>

        <form onSubmit={handleAlunoSubmit} style={{ marginBottom: "1rem" }}>
          <input
            name="nome"
            placeholder="Nome"
            value={alunoForm.nome}
            onChange={handleAlunoChange}
          />
          <input
            name="email"
            placeholder="Email"
            value={alunoForm.email}
            onChange={handleAlunoChange}
          />
          <input
            name="idade"
            placeholder="Idade"
            type="number"
            value={alunoForm.idade}
            onChange={handleAlunoChange}
          />
          <button type="submit">
            {alunoForm.id ? "Atualizar" : "Criar"} aluno
          </button>
        </form>

        <table border="1" cellPadding="6">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome</th>
              <th>Email</th>
              <th>Idade</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {alunos.map((a) => (
              <tr key={a.id}>
                <td>{a.id}</td>
                <td>{a.nome}</td>
                <td>{a.email}</td>
                <td>{a.idade}</td>
                <td>
                  <button onClick={() => handleAlunoEdit(a)}>Editar</button>
                  <button onClick={() => handleAlunoDelete(a.id)}>
                    Excluir
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      {/* ---------- NOTAS ---------- */}
      <section>
        <h2>Notas (Service 2)</h2>

        <form onSubmit={handleNotaSubmit} style={{ marginBottom: "1rem" }}>
          <input
            name="aluno_id"
            placeholder="ID do aluno"
            type="number"
            value={notaForm.aluno_id}
            onChange={handleNotaChange}
          />
          <input
            name="curso_id"
            placeholder="ID do curso"
            type="number"
            value={notaForm.curso_id}
            onChange={handleNotaChange}
          />
          <input
            name="valor"
            placeholder="Nota (0-10)"
            type="number"
            step="0.1"
            value={notaForm.valor}
            onChange={handleNotaChange}
          />
          <button type="submit">
            {notaForm.id ? "Atualizar" : "Criar"} nota
          </button>
        </form>

        <table border="1" cellPadding="6">
          <thead>
            <tr>
              <th>ID</th>
              <th>Aluno</th>
              <th>Curso</th>
              <th>Valor</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {notas.map((n) => (
              <tr key={n.id}>
                <td>{n.id}</td>
                <td>{n.aluno_id}</td>
                <td>{n.curso_id}</td>
                <td>{n.valor}</td>
                <td>
                  <button onClick={() => handleNotaEdit(n)}>Editar</button>
                  <button onClick={() => handleNotaDelete(n.id)}>
                    Excluir
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}

export default App;
