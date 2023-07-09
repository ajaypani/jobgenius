document.getElementById("recommendationForm").addEventListener("submit", async (event) => {
    event.preventDefault();
  
    const form = new FormData(event.target);
  
    try {
      const response = await fetch("/getRecommendations", {
        method: "POST",
        body: form
      });
  
      if (response.ok) {
        const recommendations = await response.json();
        displayRecommendations(recommendations);
      } else {
        console.error("Failed to get recommendations.");
      }
    } catch (error) {
      console.error("An error occurred:", error);
    }
  });
  
  function displayRecommendations(recommendations) {
    const recommendationsDiv = document.getElementById("recommendations");
    recommendationsDiv.innerHTML = "";
  
    recommendations.forEach((recommendation) => {
      const recommendationItem = document.createElement("div");
      recommendationItem.textContent = recommendation;
      recommendationsDiv.appendChild(recommendationItem);
    });
  }
  