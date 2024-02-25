// elements of edit views//
const editButtons = document.getElementsByClassName("btn-edit");
const answerText = document.getElementById("id_body");
const answerform = document.getElementById("AnswerForm");
const submitButton = document.getElementById("submitButton");


// elements of delete views//
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// function  to edit answers//
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let answerId = e.target.getAttribute("answer_id");
        let answerContent = document.getElementById(`answer${answerId}`).innerText;
        answerText.value = answerContent;
        submitButton.innerText = "Update";
        answerform.setAttribute("action", `edit_answer/${answerId}`);
    });
}

// function  to delete answers//
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let answerId = e.target.getAttribute("answer_id");
        deleteConfirm.href = `delete_answer/${answerId}`;
        deleteModal.show();
    });
}
