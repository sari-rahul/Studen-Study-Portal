console.log("Hello ")

const editButtons = document.getElementsByClassName("btn-edit");
const answerText = document.getElementById("id_body");
const answerform = document.getElementById("AnswerForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let answerId = e.target.getAttribute("answer_id");
        let answerContent = document.getElementById(`answer${answerId}`).innerText;
        answerText.value = answerContent;
        submitButton.innerText = "Update";
        answerform.setAttribute("action", `edit_answer/${answerId}`);
    });
  }
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let answerId = e.target.getAttribute("answer_id");
        deleteConfirm.href = `delete_answer/${answerId}`;
        deleteModal.show();
    });
}
