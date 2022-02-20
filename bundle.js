

const getClosestPotions = (potion)=>(potionNames.filter(txt => txt.indexOf(potion.toLowerCase().replace(/\w/, l => l.toUpperCase())) !== -1));
async function updatePotions(query) {
	const potionsearch = document.getElementById("potion-search"); 
	if (potionsearch.value === "") {
		return
	} else {
		const results = document.getElementById("potion-results");
		const closest = getClosestPotions(potionsearch.value);
		
		results.innerHTML = "";
		for (let potion of closest) {
			let ingredientsHTML = `<div class="ingredientsRowSmall">`;
			for (let ingredient of Potions[potion].ingredients) {
				ingredientsHTML += `
				<div class="box ingredient ingredientSmall" style="width:26px; height:26px;">
					<img src="${Ingredients[ingredient].img}"" width="20px" height="20px"/>
					<div class="box ingredient-textbox" style="width:max-content; text-align:center; align-items:center; margin-bottom:5px;">
						<span class="ingredient-text" style="font-size: 13px;">
						${ingredient}
						</span>
					</div>
				</div>`;
			};
			ingredientsHTML += `</div>`;
			results.innerHTML += `
			<div class="box potionRow" data-name="${potion}">
				<img src="${Potions[potion].img}" width="50px" height="50px" class="potionImageSearch"/>
				<span class="potionNameSearch">
					${potion}
				</span>
				${ingredientsHTML}
				<span class="potionPrice">
					<span class="priceAmount"> 
						${Potions[potion].price} 
					</span>
					<img src="images/gold.png" width="24px" height="24px" class="potionGold" />
				</span>
			</div>
			`;	
		};
		async function updateSelectedPotion() {
			const ingredientsRow = document.getElementById("potionIngredients");
		
			
			document.getElementById("selectedPotion").firstElementChild.src = Potions[this.getAttribute("data-name")].img;
			document.getElementById("selectedPotionName").innerHTML = this.getAttribute("data-name");
			ingredientsRow.innerHTML = "";
			for (let ingredient of Potions[this.getAttribute("data-name")].ingredients) {
				ingredientsRow.innerHTML += `
				<div class="box ingredient" style="width:45px; height:45px;" >
					<img src="${Ingredients[ingredient].img}"" width="36px" height="36px"/>
					<div class="box ingredient-textbox" style="width:max-content; text-align:center; align-items:center; margin-bottom:5px;">
						<div class="ingredient-text" style="font-size: 13px;">${ingredient}</div>
					</div>
				</div>
				`
			};
			ingredientsRow.style = `width:${45*Potions[this.getAttribute("data-name")].ingredients}px;`;
		};
		for (let element of document.getElementsByClassName("potionRow")) {
			element.addEventListener('click', updateSelectedPotion);
		};
		results.style = `top:${70 + (6 * closest.length)}%;`;
	}
};
const potionsearch = document.getElementById("potion-search"); 
potionsearch.addEventListener('change', updatePotions);