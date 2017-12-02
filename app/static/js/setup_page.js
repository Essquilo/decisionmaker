
var setup = new Vue({
    el: '#setup',
    data: {
        alternatives: [],
        criteria: [],
        question: ""
    },
    delimiters: ["[[", "]]"],
    methods: {
        validate(){
            a = !(_.isEmpty(this.alternatives));
            c = !(_.isEmpty(this.criteria));
            alternativesDefined = _.every(this.alternatives, function (alt) {
                            return alt.title != '';
                        });
            criteriaDefined = _.every(this.criteria, function (crit) {
                            return (crit.name != '' && crit.description != '' && crit.weight != 0);
                        });
            //descriptions = _.every(this.criteria.description, function (description) {
            //                return description != '';
            //            });
            //weights = _.every(this.criteria.weight, function (weight) {
            //                return weight != 0;
            //            });
            //questionDefined = function(){
            //    return this.question != '';
            //};
            questionDefined = (this.question != '');
            //console.log(a);
            //console.log(c);
            //console.log(this.alternatives);
            //console.log(this.criteria);
            //console.log(this.question);
            //console.log(titles);
            //console.log(names);
            //console.log(descriptions);
            //console.log(weights);
            //console.log(questionDefined);
            //console.log(this.question);
            //console.log((this.question != ''));
            result = (a && c && alternativesDefined && criteriaDefined && questionDefined);
            //console.log(result);
            return result;
            //return questionDefined();
        },
        submit(){
            //alert('test alert');
            if(!(this.validate())){
                alert('Please fill in all the fields or delete unwanted alternatives and criteria.');
            } else{
                alert('Data submitted');
                //submit data
                $.ajax({
                    type: "POST",
                    url: '/submit_results',
                    data: this.answers
                });
            }
        },
        addAlternative(){
            this.alternatives.push({title: ''});
            //this.submit();
        },
        addCriterion(){
            this.criteria.push({name: '', description: '', weight: 0});
        },
        removeAlternative(index){
            this.alternatives.splice(index, 1);
            console.log(this);
        },
        removeCriterion(id){
            var index = this.criteria.indexOf(id);
            this.criteria.splice(index, 1);
        }
    }
});