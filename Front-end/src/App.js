import React from 'react';
import './App.css';


class App extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      todoList: [],
      activeItem: {
        id: null,
        nomeCompleto: '',
        cpf: '',
        endereco: '',
        valorEmprestimoPretendido: 0,
      },
      editing: false,
    };
  
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

  };
  

  handleChange(e) {
    const { name, value } = e.target;

    if (name === 'cpf') {
      // Remove caracteres não numéricos do valor do CPF
      const cleanedValue = value.replace(/\D/g, '');
  
      // Verifica se o valor possui 11 dígitos
      if (cleanedValue.length === 11) {
        this.setState({
          activeItem: {
            ...this.state.activeItem,
            [name]: cleanedValue
          }
        });
      }
    } else {
      this.setState({
        activeItem: {
          ...this.state.activeItem,
          [name]: value
        }
      });
    }
  }


  handleSubmit(e) {
    e.preventDefault();

    const { nomeCompleto, cpf, endereco, valorEmprestimoPretendido } = this.state.activeItem;

    if (nomeCompleto && cpf && endereco && valorEmprestimoPretendido) {

      // Todos os campos foram preenchidos, continuar com o envio do formulário
      console.log('ITEM:', this.state.activeItem);
    
      var url = 'http://127.0.0.1:8000/api/v1/propostas/nova/';
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify({
          nomeCompleto: this.state.activeItem.nomeCompleto,
          cpf: this.state.activeItem.cpf,
          endereco: this.state.activeItem.endereco,
          valorEmprestimoPretendido: parseFloat(this.state.activeItem.valorEmprestimoPretendido)
        })
      })
      .then(response => {
        if (response.status === 201) {
          alert('Formulário inserido com sucesso!');

          window.location.reload(); // Recarrega a página

        }else {
          alert('Erro ao inserir o formulário. Por favor, tente novamente.');
        }
      })
      .catch(error => {
        console.log('ERROR:', error);
      });
      
    }else{
      // Exibir mensagem alerta informando que todos os campos são obrigatórios
      alert('Por favor, preencha os campos obrigatórios:\n- Nome\n- CPF\n- Endereço\n- Valor');
    }
}


  render(){
    var tasks = this.state.todoList

    return(
      <div className='container'>
        <div id='task-container'>
          <div id='form-wrapper'>
            
            <h5>Formulário referente a proposta de empréstimo pessoal</h5>
            
            <form onSubmit={this.handleSubmit} id='form'>

              <div className='flex-wrapper'>
                <div style={{flex: 6}}>
                  <input onChange={this.handleChange} className='form-control' id='title' type='text' name='nomeCompleto' placeholder="Nome Completo"></input>
                </div>         
              </div>

              <div className='flex-wrapper'>
                <div style={{flex: 6}}>
                  <input onChange={this.handleChange} className='form-control' id='title' type='text' name='cpf' placeholder="CPF"></input>
                </div>
              </div>

              <div className='flex-wrapper'>
                <div style={{flex: 6}}>
                  <input onChange={this.handleChange} className='form-control' id='title' type='text' name='endereco' placeholder="Endereço"></input>
                </div>
              </div>

              <div className='flex-wrapper'>
                <div style={{flex: 6}}>
                  <input onChange={this.handleChange} className='form-control' id='title' type='number' step='0.01' name='valorEmprestimoPretendido' placeholder="Valor do Empréstimo Pretendido"></input>
                </div>
              </div>
              
              <div style={{flex: 1}}>
                  <input className='btn btn-warning' id='enviar' value='Envair' type='submit' name='Add' placeholder="Add task.."></input>
                </div>
            </form>
          </div>

        </div>
      </div>
    )
  }
}

export default App;
