async function myratingslist(titleID) {
    try {
        const response = await fetch(`/ntuaflix_api/check_myratingslist/${titleID}`);
        const data = await response.json();
        return data.inmyratingslist;
    } catch (error) {
        console.error("Error checking myratingslist:", error);
        return 0;
    }
}




