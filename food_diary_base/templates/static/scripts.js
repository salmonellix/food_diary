function deleteItem(items){

			console.log('Delete clicked')
            var url = '{% url product-delete 1 2 %}';
			url = url.replace(1, items[0]);
			url = url.replace(2, items[1]);

			fetch(url, {
				method:'DELETE',
				headers:{
					'Content-type':'application/json',
					'X-CSRFToken':csrftoken,
				}
			})
		}


function countKcals()