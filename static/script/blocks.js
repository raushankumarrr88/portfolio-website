document.addEventListener("DOMContentLoaded", function () {
    const blocks = document.querySelectorAll(".main-container");
    const container = document.querySelector(".container-around");

    const colors = ["#571301", "#3a0157", "#011230", "#570143"];

    const initialOrder = Array.from(blocks);
    let currentOrder = Array.from(initialOrder);

    blocks.forEach((block, index) => {
        block.style.backgroundColor = colors[index % colors.length];

        setTimeout(() => {
            block.classList.add("appear");
        }, index * 200);

        const closeBtn = block.querySelector(".close-btn");

        block.addEventListener("click", function () {
            blocks.forEach(b => {
                b.classList.remove("selected");
                const btn = b.querySelector(".close-btn");
                btn.style.display = "none";
            });

            currentOrder = currentOrder.filter(b => b !== this);

            container.prepend(this);

            requestAnimationFrame(() => {
                this.classList.add("selected");
                closeBtn.style.display = "block";

                currentOrder.forEach(b => {
                    container.append(b);
                });

                currentOrder = Array.from(initialOrder);
            });
        });

        closeBtn.addEventListener("click", function (e) {
            e.stopPropagation();
            block.classList.remove("selected");
            closeBtn.style.display = "none";

            initialOrder.forEach(b => {
                container.append(b);
            });
        });
    });
});
