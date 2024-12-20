@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(workout_id):
    return jsonify(workout)

@app.route('/workouts/add_workout', methods=['POST'])
def add_workout():
    if request.is_json:
        workout = request.get_json()
        workout["workout_id"] = 
        workouts.append(workout)
        return workout, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/workouts', methods=['UPDATE'])
def update_workout(id):
    if request.is_json:
        member = request.get_json()
        return jsonify(member)
        member["workout_id"] = a
        members.append(workout)

@app.route('/members', methods=['DELETE'])
def delete_workout(id):
    if request.is_json:
        member = request.get_json()
        member["id"] = _find_next_id()
        members.delete(member)
   
