document.addEventListener("DOMContentLoaded", function () {
    const taskItems = document.querySelectorAll(".task-item");

    taskItems.forEach((item) => {
        item.addEventListener("click", function () {
            const modalId = item.getAttribute("data-bs-target");
            const modal = document.querySelector(modalId);
            const bootstrapModal = new bootstrap.Modal(modal);
            bootstrapModal.show();
        });
    });
});
