import axios from 'axios';

export function getStudents() {
  return axios.get('http://127.0.0.1:8000/')
    .then(response => response.data)
}

export function deleteStudent(stuid) {
  return axios.delete('http://127.0.0.1:8000/delete/' + stuid , {
   method: 'DELETE',
   headers: {
     'Accept':'application/json',
     'Content-Type':'application/json'
   }
  })
  .then(response => response.data)
}

export function addStudent(student){
  return axios.post('http://127.0.0.1:8000/create', {
    studentId:null,
    firstname:student.firstname.value,
    lastname:student.lastname.value,
    registrationNo:student.registrationNo.value,
    email:student.email.value,
    course:student.course.value
  })
    .then(response=>response.data)
}

export function updateStudent(stuid, student) {
  return axios.put('http://127.0.0.1:8000/update/' + stuid, {
    firstname:student.firstname.value,
    lastname:student.lastname.value,
    registrationNo:student.registrationNo.value,
    email:student.email.value,
    course:student.course.value
  })
   .then(response => response.data)
}