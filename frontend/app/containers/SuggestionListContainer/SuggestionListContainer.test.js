import React from 'react';
import renderer from 'react-test-renderer';
import SuggestionListContainer from './';
// import data from './SuggestionListContainer.json';

describe('<SuggestionListContainer />', () => {
    it('Renders an empty SuggestionListContainer', () => {
        const componentJson = renderer
            .create(<SuggestionListContainer />)
            .toJSON();
        expect(componentJson).toBeTruthy();
    });

    /*
    it('Renders SuggestionListContainer with data', () => {
        const componentJson = renderer
            .create(<SuggestionListContainer {...data} />)
            .toJSON();
        expect(componentJson).toMatchSnapshot();
    });
    */
});
